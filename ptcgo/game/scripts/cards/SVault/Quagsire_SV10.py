from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.data_utils import Activations


def _water_energy(card):
    return energy_provides_type(card, PokemonTypes.WATER.value)


async def wash_out(ctx):
    """Move a Water Energy from 1 of your Benched Pokemon to your Active."""
    await move_energy_between(predicate=_water_energy, count=1, from_pool="bench",
                              to_pool="active")(ctx)


_can_wash_out = can_move_energy(predicate=_water_energy, from_pool="bench", to_pool="active")

card = PokemonCardDef(
    guid="c53fa948-b8b6-532a-9b98-1d5405319ac9",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Ability(
            title="Wash Out",
            game_text="As often as you like during your turn (before your attack), you may move a Water Energy from 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_can_wash_out,
            effect=wash_out,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage times the amount of Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.WATER), 20, base=60),
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.data_utils import Activations


def _fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def flash_fire(ctx):
    """Move a Fire Energy from 1 of your Pokemon to this Pokemon."""
    await move_energy_between(
        predicate=_fire_energy, count=1, from_pool="any", to_pool="any",
        to_pred=lambda pokemon, context: pokemon is context.source,
    )(ctx)


_can_flash_fire = can_move_energy(predicate=_fire_energy)

card = PokemonCardDef(
    guid="f46d1d42-ff21-5633-84d5-0eaae89c57bb",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonEX.Name",
    display_name="Flareon-EX",
    searchable_by=["Flareon-EX", "Basic", "EX", "FlareonEX"],
    subtypes=["Basic", "EX"],
    collector_number=10006,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Ability(
            title="Flash Fire",
            game_text="Once during your turn (before your attack), you may move a Fire Energy from 1 of your Pok\u00e9mon to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_can_flash_fire,
            effect=flash_fire,
        ),
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.FIRE), per=20, base=50),
        ),
    ],
)
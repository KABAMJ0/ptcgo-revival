from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.data_utils import Activations


def _grass_energy(card):
    return energy_provides_type(card, PokemonTypes.GRASS.value)


async def energy_trans(ctx):
    """Take 1 Grass Energy attached to 1 of your Pokemon and attach it to a
    different one."""
    await move_energy_between(predicate=_grass_energy, count=1,
                              from_pool="any", to_pool="any")(ctx)


_can_energy_trans = can_move_energy(predicate=_grass_energy)


card = PokemonCardDef(
    guid="3eaeebc0-2fe5-50bb-a317-1199c92031a9",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="BASE1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Energy Trans",
            game_text="As often as you like during your turn (before your attack), you may take 1 Grass Energy card attached to 1 of your Pok\u00e9mon and attach it to a different one. This power can't be used if Venusaur is Asleep, Confused, or Paralyzed.",
            activation=Activations.UNLIMITED,
            condition=_can_energy_trans,
            effect=energy_trans,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 4},
            damage=60,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.data_utils import Activations


def _fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def gather_fire(ctx):
    """Take 1 Fire Energy card attached to 1 of your other Pokemon and attach
    it to Charmander."""
    await move_energy_between(
        predicate=_fire_energy, count=1, from_pool="any", to_pool="any",
        to_pred=lambda pokemon, context: pokemon is context.source,
    )(ctx)


_can_gather_fire = can_move_energy(predicate=_fire_energy)

card = PokemonCardDef(
    guid="3d6d1c6b-8a53-5778-92e3-a3251f0ebd3d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Ability(
            title="Gather Fire",
            game_text="Once during your turn (before your attack), you may take 1 Fire Energy card attached to 1 of your other Pok\u00e9mon and attach it to Charmander. This power can't be used if Charmander is Asleep, Confused, or Paralyzed.",
            activation=Activations.ONCE_PER_TURN,
            condition=_can_gather_fire,
            effect=gather_fire,
        ),
        Attack(
            title="Fire Tail",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
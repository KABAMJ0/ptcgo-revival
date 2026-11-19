from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.passives_common import shield_source_next_turn
from ptcgo.game.card_effects.support_common import entity_name


def _unown_named(pokemon):
    return pokemon is not None and "Unown" in entity_name(pokemon)


async def _quicken(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if _unown_named(pokemon):
            await shield_source_next_turn(prevent=True, effects_too=True,
                                          target=pokemon)(ctx)


card = PokemonCardDef(
    guid="d1fbe51d-8ea2-563a-b0e9-df7e08d264d4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownQ.Name",
    display_name="Unown [Q]",
    searchable_by=["Unown [Q]", "Basic", "UnownQ"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Quicken]",
            activation=Activations.ONCE_PER_TURN,
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, prevent all effects of attacks, including damage, done to any of your Pok\u00e9mon with Unown in its name during your opponent's next turn. If you have more than 1 Unown [Q] in play, use only 1 [Quicken] each turn. This power can be used even if Unown [Q] is Asleep, Confused, or Paralyzed.",
            effect=flip_gate(then=_quicken),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
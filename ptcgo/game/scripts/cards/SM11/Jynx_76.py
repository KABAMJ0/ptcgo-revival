from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import move_counters_ability


_move_counters, _can_move = move_counters_ability(1, "mine")

card = PokemonCardDef(
    guid="e6372ae5-ad78-541b-b0ac-d0b8fddfb811",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Ability(
            title="Ominous Posture",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_can_move,
            effect=_move_counters,
        ),
        Attack(
            title="Attract Smack",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
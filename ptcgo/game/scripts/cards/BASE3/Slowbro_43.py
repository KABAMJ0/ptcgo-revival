from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="535640a5-480a-5e13-9f11-5fcc572aa371",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Strange Behavior",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to Slowbro as long as you don't Knock Out Slowbro. This power can't be used if Slowbro is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)
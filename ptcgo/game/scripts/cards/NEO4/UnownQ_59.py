from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

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
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, prevent all effects of attacks, including damage, done to any of your Pok\u00e9mon with Unown in its name during your opponent's next turn. If you have more than 1 Unown [Q] in play, use only 1 [Quicken] each turn. This power can be used even if Unown [Q] is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
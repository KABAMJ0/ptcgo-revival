from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="836b5e80-0ec9-59a5-bf54-ff145849d99e",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownU.Name",
    display_name="Unown [U]",
    searchable_by=["Unown [U]", "Basic", "UnownU"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Undo]",
            game_text="Once during your turn (before your attack), if you have Unown [U], Unown [N], Unown [D], and Unown [O] on your Bench, you may return your Active Pok\u00e9mon and all cards attached to it to your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
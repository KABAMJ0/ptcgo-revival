from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63e76787-7e48-59bc-b9ee-ffe9313ddd18",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=594,
    abilities=[
        Ability(
            title="Gentle Fin",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may put a Basic Pok\u00e9mon with 70 HP or less from your discard pile onto your Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
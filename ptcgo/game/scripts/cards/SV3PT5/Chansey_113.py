from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca29b636-d4ea-5652-844e-bd79fa4a0ebc",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Ability(
            title="Lucky Bonus",
            game_text="If you took this Pok\u00e9mon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench. If you put this Pok\u00e9mon onto your Bench in this way, flip a coin. If heads, take 1 more Prize card.",
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
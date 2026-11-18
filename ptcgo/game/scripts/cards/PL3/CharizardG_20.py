from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2489601a-5938-5c95-96c5-56009a25e093",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardG.Name",
    display_name="Charizard G",
    searchable_by=["Charizard G", "Basic", "SP", "CharizardG"],
    subtypes=["Basic", "SP"],
    collector_number=20,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=6,
    abilities=[
        Attack(
            title="Flame Jet",
            game_text="Flip a coin. If heads, this attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="253993bd-d480-54e0-90c6-d9691570f58a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=174,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Ability(
            title="Bouffer",
            game_text="This Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Damage Rush",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb5c5248-dc09-5511-ac6e-72dc897c30ae",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=185,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Ability(
            title="Flower Curtain",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon that don't have a Rule Box by attacks from your opponent's Pok\u00e9mon. (Pok\u00e9mon ex, Pok\u00e9mon V, etc. have Rule Boxes.)",
            effect=unimplemented,
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
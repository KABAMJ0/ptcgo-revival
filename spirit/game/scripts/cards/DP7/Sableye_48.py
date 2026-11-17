from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba84cedb-e64a-5f04-98e7-5b96bd6484f7",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=302,
    abilities=[
        Ability(
            title="Overeager",
            game_text="If Sableye is your Active Pok\u00e9mon at the beginning of the game, you go first. (If each player's Active Pok\u00e9mon has the Overeager Pok\u00e9-Body, this power does nothing.)",
            effect=unimplemented,
        ),
        Attack(
            title="Impersonate",
            game_text="Search your deck for a Supporter card and discard it. Shuffle your deck afterward. Then, use the effect of that card as the effect of this attack.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Overconfident",
            game_text="If the Defending Pok\u00e9mon has fewer remaining HP than Sableye, this attack's base damage is 40.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bad06b9d-e824-54ba-8659-afaa7852225e",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    display_name="Poliwhirl",
    searchable_by=["Poliwhirl", "Stage 1", "Poliwhirl"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Belly Drum",
            game_text="Put 3 damage counters on Poliwhirl. If this doesn't Knock Out Poliwhirl, search your deck for 2 Basic Energy cards and attach them to Poliwhirl. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Water Gun",
            game_text="Does 30 damage plus 10 more damage for each Water Energy attached to Poliwhirl but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
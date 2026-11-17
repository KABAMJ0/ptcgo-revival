from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37cb2c86-d943-595e-981f-912e8c2b2b0d",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Attack(
            title="Poisonous Whip",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Tentacular Panic",
            game_text="Flip a coin until you get tails. This attack does 90 damage for each heads. If the first flip is tails, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
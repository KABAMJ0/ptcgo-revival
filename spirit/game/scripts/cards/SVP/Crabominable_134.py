from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd33c157-c1af-574f-80f6-8249eb8844db",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name",
    display_name="Crabominable",
    searchable_by=["Crabominable", "Stage 1", "Crabominable"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    family_id=740,
    abilities=[
        Ability(
            title="Food Prep",
            game_text="Attacks used by this Pok\u00e9mon cost Colorless less for each Kofu card in your discard pile.",
            effect=unimplemented,
        ),
        Attack(
            title="Haymaker",
            game_text="During your next turn, this Pok\u00e9mon can't use Haymaker.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 4},
            damage=250,
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="057ff611-d38f-5d71-8810-0412bc7ff4bc",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name",
    display_name="Crabominable",
    searchable_by=["Crabominable", "Stage 1", "Crabominable"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    family_id=739,
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
            locks_next_turn=True,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1f97b64-5ddc-5481-aa39-26520dabd2d5",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmora.Name",
    display_name="Glimmora",
    searchable_by=["Glimmora", "Stage 1", "Glimmora"],
    subtypes=["Stage 1"],
    collector_number=126,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Ability(
            title="Shattering Crystal",
            game_text="When this Pok\u00e9mon is Knocked Out, flip a coin. If heads, your opponent can't take any Prize cards for it.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Petals",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, put 6 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
    ],
)
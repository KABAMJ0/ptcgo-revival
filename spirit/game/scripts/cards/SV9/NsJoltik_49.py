from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31acfa0b-a715-5ff6-8db8-15e41cfa6205",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsJoltik.Name",
    display_name="N's Joltik",
    searchable_by=["N's Joltik", "Basic", "NsJoltik"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Zapping Short",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon. If you discarded a Pok\u00e9mon Tool in this way, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
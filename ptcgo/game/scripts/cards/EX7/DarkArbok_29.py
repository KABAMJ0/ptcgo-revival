from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2000ec48-72bc-50f6-816d-0306fee089ee",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkArbok.Name",
    display_name="Dark Arbok",
    searchable_by=["Dark Arbok", "Stage 1", "DarkArbok"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Swallow Up",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon and Dark Arbok. If the Defending Pok\u00e9mon has fewer remaining HP than Dark Arbok's, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Extra Poison",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, the Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
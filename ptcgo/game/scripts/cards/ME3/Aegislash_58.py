from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f4a01e79-db8b-5adf-ab16-02026c5938ea",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=58,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
        Attack(
            title="Metal Slash",
            game_text="During your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=230,
            effect=unimplemented,
        ),
    ],
)
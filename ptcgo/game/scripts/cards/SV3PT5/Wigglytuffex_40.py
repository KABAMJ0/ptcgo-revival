from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dffffad4-042c-55cd-812a-beed156ce630",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuffex.Name",
    display_name="Wigglytuff ex",
    searchable_by=["Wigglytuff ex", "Stage 1", "ex", "Wigglytuffex"],
    subtypes=["Stage 1", "ex"],
    collector_number=40,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Ability(
            title="Expanding Body",
            game_text="If this Pok\u00e9mon has any Special Energy attached, it gets +100 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Friend Tackle",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
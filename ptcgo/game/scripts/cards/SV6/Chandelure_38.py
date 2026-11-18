from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d9cd2eb4-ad7d-56fb-b3ac-6e047e8471cb",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Alluring Light",
            game_text="Once during your turn, you may have each player draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Mind Ruler",
            game_text="This attack does 30 damage for each card in your opponent's hand.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
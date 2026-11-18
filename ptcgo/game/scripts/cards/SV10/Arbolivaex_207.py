from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="294c847d-1281-51cd-bc25-847c080af24a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbolivaex.Name",
    display_name="Arboliva ex",
    searchable_by=["Arboliva ex", "Stage 2", "ex", "Arbolivaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=207,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Oil Salvo",
            game_text="Choose 1 of your opponent's Pok\u00e9mon 6 times. (You can choose the same Pok\u00e9mon more than once.) For each time you chose a Pok\u00e9mon, do 20 damage to it. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Aroma Shot",
            game_text="This Pok\u00e9mon recovers from all Special Conditions.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)
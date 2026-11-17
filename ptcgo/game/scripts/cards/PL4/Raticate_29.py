from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca1fcd71-3b60-5328-8d35-36f485731e1e",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Recruit",
            game_text="Look at your opponent's hand, choose a Supporter card you find there, and discard it. Then, use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Extend Fang",
            game_text="If Raticate has a Pok\u00e9mon Tool card attached to it, this attack does 20 damage plus 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
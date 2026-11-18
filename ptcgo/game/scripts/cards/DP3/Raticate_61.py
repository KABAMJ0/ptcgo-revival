from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29fd30f7-87db-5b39-805d-ec6a910e27ec",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Gnaw Off",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(70)),
        ),
        Attack(
            title="Sneaky Attack",
            game_text="If Raticate has any Darkness Energy attached to it, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
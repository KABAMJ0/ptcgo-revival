from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e64ec58d-fc1b-5fd3-a024-ec7b322ae230",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    display_name="Sentret",
    searchable_by=["Sentret", "Basic", "Sentret"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=161,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(30)),
        ),
    ],
)
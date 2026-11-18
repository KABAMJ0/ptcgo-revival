from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="766b793a-7804-5519-ba2a-f38b621c24e7",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name",
    display_name="Floatzel",
    searchable_by=["Floatzel", "Stage 1", "Floatzel"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    family_id=418,
    abilities=[
        Attack(
            title="Screw Tail",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
        Attack(
            title="Water Gun",
            game_text="Does 40 damage plus 20 more damage for each Water Energy attached to Floatzel but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cefd7886-ae87-5281-b393-6a427c2aa681",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1", "Lairon"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Granite Head",
            game_text="During your opponent's next turn, any damage done to Lairon by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=protect_next_turn(reduce=10),
        ),
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(50)),
        ),
    ],
)
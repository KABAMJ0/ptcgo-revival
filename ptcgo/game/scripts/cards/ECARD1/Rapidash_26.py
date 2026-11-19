from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ac32c59a-8a32-54fe-8d84-72988de8a83b",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1", "Rapidash"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Attack(
            title="Overrun",
            game_text="If your opponent has any Benched Pok\u00e9mon, flip a coin. If heads, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=composed(lambda ctx: ctx.deal_damage(20), flip_gate(snipe_attack(10, pool="bench", count=1, apply_modifiers=False))),
        ),
        Attack(
            title="Flame Tail",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
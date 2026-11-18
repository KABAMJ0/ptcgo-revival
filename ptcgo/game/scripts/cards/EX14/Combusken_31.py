from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9204422-a037-57d2-b511-4a90c15a78a1",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    display_name="Combusken",
    searchable_by=["Combusken", "Stage 1", "Combusken"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(50)),
        ),
    ],
)
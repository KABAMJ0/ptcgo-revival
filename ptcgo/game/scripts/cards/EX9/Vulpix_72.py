from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b824be3-c882-59b5-8cfc-645293d64af2",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic", "Vulpix"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(30)),
        ),
    ],
)
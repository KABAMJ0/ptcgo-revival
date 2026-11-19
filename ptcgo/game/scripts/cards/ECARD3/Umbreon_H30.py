from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5a922e4-7c78-51b0-bd5b-a4b3d227b33a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Dark Gaze",
            game_text="As long as Umbreon is your Active Pok\u00e9mon, Benched Pok\u00e9mon (yours and your opponent's) can't use Pok\u00e9-Powers.",
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Claws",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(40)),
        ),
    ],
)
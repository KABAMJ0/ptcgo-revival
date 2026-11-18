from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01a46527-a206-56c8-97c3-c1ea895c9b08",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Overzealous",
            game_text="If your opponent has any Pok\u00e9mon-ex in play, each of Machamp's attacks does 30 more damage to the Defending Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Brick Smash",
            game_text="This attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 60 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(90)),
        ),
    ],
)
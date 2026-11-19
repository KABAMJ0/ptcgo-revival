from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="0b76053a-b335-52e2-9236-a9fbbf5d7f4b",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2", "Exploud"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Mega Throw",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 60 damage plus 40 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
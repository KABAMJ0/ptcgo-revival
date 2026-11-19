from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="bf29f4ee-805e-514c-ba44-69f8729fdf34",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizorex.Name",
    display_name="Scizor ex",
    searchable_by=["Scizor ex", "Stage 1", "ex", "Scizorex"],
    subtypes=["Stage 1", "ex"],
    collector_number=108,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=212,
    abilities=[
        Ability(
            title="Danger Perception",
            game_text="As long as Scizor ex's remaining HP is 60 or less, Scizor ex does 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to Scizor ex by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Cross-Cut",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_evolution_pokemon(ctx.defender), 30),
        ),
    ],
)
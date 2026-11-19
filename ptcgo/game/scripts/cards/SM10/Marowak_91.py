from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, active_is, has_tool

card = PokemonCardDef(
    guid="0553685d-34ad-527a-afd0-e0aa35647894",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Bone Rush",
            game_text="Flip a coin until you get tails. This attack does 50 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="x",
            effect=flip_damage(per_heads=50, until_tails=True),
        ),
        Attack(
            title="Assault Boom",
            game_text="If your opponent's Active Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=bonus_if(active_is(has_tool), 70),
        ),
    ],
)
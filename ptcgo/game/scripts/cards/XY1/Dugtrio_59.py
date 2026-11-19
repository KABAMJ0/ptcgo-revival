from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack, spread_damage

card = PokemonCardDef(
    guid="fd6819cc-42b1-5a04-835c-2415eb045b8b",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Dugtrio"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Earthquake",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=spread_damage(10, side="mine", also_base=True),
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)
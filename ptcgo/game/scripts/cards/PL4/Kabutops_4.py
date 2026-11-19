from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_for_bonus, snipe_attack
from ptcgo.game.card_effects.trainers import any_of, named

card = PokemonCardDef(
    guid="3d15fa26-fe1b-5c29-811c-6384b9402eb3",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2", "Kabutops"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Primal Scythe",
            game_text="You may discard Helix Fossil, Dome Fossil, or Old Amber from your hand. If you do, this attack does 20 damage plus 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=discard_for_bonus(predicate=any_of(named("helix fossil"), named("dome fossil"), named("old amber")), max_count=1, flat=50),
        ),
        Attack(
            title="Rock Slide",
            game_text="Does 10 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=snipe_attack(10, pool="bench", count=2, apply_modifiers=False),
        ),
    ],
)
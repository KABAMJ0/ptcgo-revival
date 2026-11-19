from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="1f94dd8c-5b31-5775-bbf5-6485bc423edc",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1", "Roserade"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Spike Whip",
            game_text="If Budew is anywhere under Roserade, choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
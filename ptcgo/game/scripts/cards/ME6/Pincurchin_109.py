from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="9c79ee26-57b9-5e3b-a219-72c25c0a7010",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name",
    display_name="Pincurchin",
    searchable_by=["Pincurchin", "Basic", "Pincurchin"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Attack(
            title="Energy Crush",
            game_text="This attack does 20 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 20),
        ),
    ],
)
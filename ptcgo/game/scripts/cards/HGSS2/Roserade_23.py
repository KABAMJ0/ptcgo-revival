from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0460ae2d-53e1-5634-8f5c-cbb00c23c825",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1", "Roserade"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Ability(
            title="Energy Signal",
            game_text="When you attach a Grass Energy card or Psychic Energy card from your hand to Roserade during your turn, you may use this power. If you attach a Grass Energy card, the Defending Pok\u00e9mon is now Confused. If you attach a Psychic Energy card, the Defending Pok\u00e9mon is now Poisoned. This power can't be used if Roserade is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Blow",
            game_text="Does 20 damage times the amount of Energy attached to Roserade.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
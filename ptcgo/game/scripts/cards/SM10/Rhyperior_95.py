from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7ad0cd1-6002-57e1-b350-8ec167f5c5ec",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=95,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Hefty Cannon",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Break Ground",
            game_text="This attack does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=spread_damage(20, side="mine", also_base=True),
        ),
    ],
)
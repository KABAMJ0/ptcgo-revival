from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="b5c3de25-efd1-53e3-ad19-410d2db21b46",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Let's Have a Blast",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, flip a coin. If heads, the Attacking Pok\u00e9mon is Knocked Out.",
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Fumes",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
    ],
)
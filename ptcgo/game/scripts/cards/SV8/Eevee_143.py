from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16a8a44a-7ebf-5d76-bead-70a1ab1a18c3",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Boosted Evolution",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, it can evolve during your first turn or the turn you play it.",
            effect=unimplemented,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)
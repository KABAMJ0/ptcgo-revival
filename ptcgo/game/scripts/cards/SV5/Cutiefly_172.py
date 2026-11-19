from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="650acd1b-fc7b-58c1-a934-d227cce14cfd",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    display_name="Cutiefly",
    searchable_by=["Cutiefly", "Basic", "Cutiefly"],
    subtypes=["Basic"],
    collector_number=172,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=742,
    abilities=[
        Attack(
            title="Mini Drain",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=heal_attack(10),
        ),
    ],
)
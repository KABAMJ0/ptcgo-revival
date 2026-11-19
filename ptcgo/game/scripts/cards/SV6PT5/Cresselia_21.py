from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16484e2e-42f6-5ab7-935a-7148e25958b0",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=488,
    abilities=[
        Attack(
            title="Healing Pirouette",
            game_text="Heal 20 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=heal_targets(20, scope="each_own"),
        ),
        Attack(
            title="Crescent Purge",
            game_text="You may turn 1 of your face-down Prize cards face up. If you do, this attack does 80 more damage. (That Prize card remains face up for the rest of the game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
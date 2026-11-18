from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import smokescreen_attack

card = PokemonCardDef(
    guid="36772a89-f279-5af9-adee-b52568331ac3",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Ability(
            title="Heal Block",
            game_text="If you have Lunatone in play, damage counters can't be removed from any Pok\u00e9mon (both yours and your opponent's). (Damage counters can still be moved.)",
            effect=unimplemented,
        ),
        Attack(
            title="Sun Flash",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=smokescreen_attack(),
        ),
    ],
)
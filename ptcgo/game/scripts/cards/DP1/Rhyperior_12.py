from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack, lock_self_attack

card = PokemonCardDef(
    guid="369f20bd-c165-5612-b3ce-d1e361b7d809",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Ability(
            title="Earth Fissure",
            game_text="Once during your turn, when you play Rhyperior from your hand to evolve 1 of your Pok\u00e9mon, you may discard the top 3 cards from your opponent's deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Wrecker",
            game_text="This attack's damage isn't affected by Weakness or Resistance. Rhyperior can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=composed(
                ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
                then=lock_self_attack(0),
            ),
        ),
    ],
)
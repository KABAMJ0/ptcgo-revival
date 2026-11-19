from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import no_retreat_passive, opposing_active, is_in_active_spot
from ptcgo.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="c9e17862-fda1-5435-ad63-30ac4b63f79e",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 2", "Omastar"],
    subtypes=["Stage 2"],
    collector_number=139,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Primordial Tentacles",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon can't retreat.",
            passive=no_retreat_passive(lambda p, c: opposing_active(p, c) and is_in_active_spot(c)),
        ),
        Attack(
            title="Aqua Split",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2},
            damage=90,
            effect=snipe_attack(30, pool='bench', count=2, apply_modifiers=False, also_base=True),
        ),
    ],
)
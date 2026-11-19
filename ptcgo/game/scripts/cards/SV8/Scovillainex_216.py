from ptcgo.game.card_effects.attacks_common import damage_counters_on
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import unimplemented, PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive

class DoubleTypePassive(Passive):
    """As long as this Pokemon is in play it is both Grass and Fire."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        live = list(types or [])
        for member in (PokemonTypes.GRASS.value, PokemonTypes.FIRE.value):
            if member not in live:
                live.append(member)
        return live


card = PokemonCardDef(
    guid="d55c858a-b2b0-5ba0-a664-762a8470a8e8",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillainex.Name",
    display_name="Scovillain ex",
    searchable_by=["Scovillain ex", "Stage 1", "ex", "Scovillainex"],
    subtypes=["Stage 1", "ex"],
    collector_number=216,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pok\u00e9mon is in play, it is Grass and Fire type.",
            passive=DoubleTypePassive(),
        ),
        Attack(
            title="Spicy Rage",
            game_text="This attack does 70 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 70, base=10),
        ),
    ],
)
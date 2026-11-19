from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import def_for
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.card_effects.attacks_common import condition_attack

class FrenzyPassive(Passive):
    """Attacks do 40 more to the Defending Pokemon while the opponent has any of
    the named Pokemon in play."""

    NAMES = ('Kyogre', 'Kyogre ex', 'Groudon', 'Groudon ex')

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.attacker is None or carrier_pokemon(carrier) is not calc.attacker:
            return
        if not getattr(calc, "to_active", False):
            return
        for player_id in calc.board.player_ids:
            if player_id == calc.attacker.owning_player_id:
                continue
            for pokemon in calc.board.pokemon_in_play(player_id):
                definition = def_for(pokemon.archetype_id)
                if definition is not None and definition.display_name in self.NAMES:
                    calc.amount += 40
                    return



card = PokemonCardDef(
    guid="d0e6ce10-27b4-55b0-b4e7-0058f32df1ac",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquazaex.Name",
    display_name="Rayquaza ex",
    searchable_by=["Rayquaza ex", "Basic", "EX", "Rayquazaex"],
    subtypes=["Basic", "EX"],
    collector_number=39,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.WATER,
    family_id=384,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="As long as your opponent has Kyogre, Kyogre ex, Groudon, or Groudon ex in play, Rayquaza ex's attacks do 40 damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=FrenzyPassive(),
        ),
        Attack(
            title="Dragon Bind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. If both are tails, this attack does nothing. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)